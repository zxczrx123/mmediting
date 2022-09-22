# Copyright (c) OpenMMLab. All rights reserved.
import torch

from mmedit.models.editors.stylegan3.stylegan3_utils import (
    apply_fractional_pseudo_rotation, apply_fractional_rotation,
    apply_fractional_translation, apply_integer_translation)


def test_integer_transformation():
    x = torch.randn(1, 3, 16, 16)
    t = torch.randn(2)
    z, m = apply_integer_translation(x, t[0], t[1])
    print(z.shape)
    print(m.shape)


def test_fractional_translation():
    x = torch.randn(1, 3, 16, 16)
    t = torch.randn(2)
    z, m = apply_fractional_translation(x, t[0], t[1])
    print(z.shape)
    print(m.shape)


def test_fractional_rotation():
    angle = torch.randn([])
    x = torch.randn(1, 3, 16, 16)
    ref, ref_mask = apply_fractional_rotation(x, angle)
    print(ref.shape)
    print(ref_mask.shape)


def test_fractional_pseduo_rotation():
    angle = torch.randn([])
    x = torch.randn(1, 3, 16, 16)
    ref, ref_mask = apply_fractional_pseudo_rotation(x, angle)
    print(ref.shape)
    print(ref_mask.shape)
